# SMEL IOT Project
 Stench monitorization and elimination project (The SMEL project)

## Description
 This project is an IOT project designed to help monitor stench levels at closed bathrooms and notify the users.
 This project has used 2 main platforms to achieve its goals.

### Tinkercad
 Tinkercad is an IOT simulation platform that allows the users to simulate IOT circuits without using real hardware.
 Link to this project's simulation can be found [here](https://www.tinkercad.com/things/kbGtyZ7RC7A?sharecode=bsSNT1kcpRtRGaKTISnYngf6-nqtqDB0CzEVSLHbJLY).

### ThingSpeak
 "ThingSpeak is an IoT analytics platform service that allows you to aggregate, visualize, and analyze live data streams in the cloud." - ThingSpeak website.
 This platform allowed us to display simulated data as if it was being sent from our IOT circuit to ThingSpeak, and analyse said data.
 Link to this project's cloud and analysis using ThingSpeak can be found [here](https://thingspeak.com/channels/2229771).

## Data Generation
 Because Tinkercad does not allow usage of the internet from within the simulation, I instead chose to simulate the data using a simple python script.
 That script will generate random data and will send it to ThingSpeak to display. Said python script can be found in this repository as "DataGeneration.py".

## Project Specification Document
 The project's specification document can be found [here](https://docs.google.com/document/d/1NXfo-tR__H7e0ITNib-rNwuwHWvR8rO7eeliOEmaOOQ/edit?usp=sharing).
