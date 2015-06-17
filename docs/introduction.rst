============
Introduction
============

Aircraft design has traditionally been based on performance characteristics, carrying capacity, and operational efficiency.  
With FAA's increasingly stringent specifications on aircraft noise, aircraft designers are increasing the importance of aircraft noise in their designs.  
Design engineers can use :abbr:`OpenMDAO (Open Multidisciplinary Design Analysis and Optimization)` to arrive at a combination of various design variables that optimizes several performance characteristics.
:abbr:`ANOPP2 (Aircraft NOise Prediction Program 2)` is a tool available to aircraft design engineers for predicting noise from the aircraft at various observer locations. 
:abbr:`AOIC (ANOPP2 OpenMDAO Interface Code)` is an interface code, written in Python, between ANOPP2 and OpenMDAO for the purpose of minimizing aircraft noise. 
Aircraft design engineers can include noise as one of the parameters to be optimized by using AOIC to bring aircraft noise, predicted by ANOPP2, into OpenMDAO.
A demonstration case is provided that predicts sideline noise during takeoff for the purpose of demonstrating the functionality of the AOIC.  
During takeoff, one of the certification microphone locations is on the sideline, measured in terms of :abbr:`EPNL (Effective Perceived Noise Level)`.
The sideline microphone location should be at the maximum noise location; this sample case demonstrates the use of AOIC to determine this location. 

