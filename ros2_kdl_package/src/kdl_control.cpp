

#include "kdl_control.h"

KDLController::KDLController(KDLRobot &_robot)
{
    robot_ = &_robot;
}

Eigen::VectorXd KDLController::idCntr(KDL::JntArray &_qd,
                                      KDL::JntArray &_dqd,
                                      KDL::JntArray &_ddqd,
                                      double _Kp, double _Kd)
{
    // read current state
    Eigen::VectorXd q = robot_->getJntValues();
    Eigen::VectorXd dq = robot_->getJntVelocities();

    // calculate errors
    Eigen::VectorXd e = _qd.data - q;
    Eigen::VectorXd de = _dqd.data - dq;

    Eigen::VectorXd ddqd = _ddqd.data;
    return robot_->getJsim() * (ddqd + _Kd*de + _Kp*e)
            + robot_->getCoriolis() + robot_->getGravity() /*friction compensation?*/;
}

/* Eigen::VectorXd KDLController::idCntr(KDL::Frame &_desPos,
                                      KDL::Twist &_desVel,
                                      KDL::Twist &_desAcc,
                                      double _Kpp, double _Kpo,
                                      double _Kdp, double _Kdo)
{

} */

KDL::JntArray KDLController::velocity_ctrl_null(KDL::Jacobian J, 
                                    Eigen::Vector3d error_position,
                                    double Kp)
                                                
{
    unsigned int nj = robot_->getNrJnts();
    Eigen::MatrixXd J_pinv = pseudoinverse(robot_->getEEJacobian().data);
    
    Eigen::VectorXd qd_vec = J_pinv * error_position * Kp;

    KDL::JntArray qd(nj);

    for (int i =0; i<nj; i++) qd.data << qd_vec(i);
    
    return qd;
}

