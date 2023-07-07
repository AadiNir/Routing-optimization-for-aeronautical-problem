# Routing-optimization-for-aeronautical-problem
BACKGROUND
In this assignment, you will address a real-world problem of routing optimisation for
aeronautical networks. There are thousands of airplanes flying over the North-Atlantic every
day, as seen in Fig. 1, where each black dot represents an airplane. In order to provide
Internet access to passengers onboard, each airplane needs to find an optimal data packet
routing path to a ground station (GS) in terms of one or two and more objectives to be
optimized.
![image](https://github.com/AadiNir/Routing-optimization-for-aeronautical-problem/assets/96436873/f166165f-f00e-482a-b3fe-ef79fd029e61)
In order to find an optimal data packet routing path, there are two metrics to be considered,
end-to-end data transmission rate and end-to-end latency.
The end-to-end latency is the sum of all delay imposed by each link. For example, a routing
path is:
Airplane-5 --> Airplane-3 --> GS-1
The delay imposed by each link is 50 milliseconds (ms). So, the end-to-end latency of the
routing path
Airplane-5 --> Airplane-3 --> GS-1 = 100 ms
The end-to-end data transmission rate is the minimum transmission rate of each link in the
routing path. For example, a routing path is
Airplane-5 --> Airplane-3 --> GS-1
The data transmission rate between Airplane-5 and Airplane-3 is 52.857 Mbps, and the data
transmission rate
between Airplane-3 and GS-1 is 43.505 Mbps, then the end-to-end data transmission rate of
the rouEng path
Airplane-5 --> Airplane-3 --> GS-1 = 43.505 Mbps.
Explicitly, a link’s transmission rate is determined by the distance of a pair of communicaEng
airplanes, which is given in Table 1. For example, if the distance between Airplane-5 and
Airplane-3 is 350 km, so 300 km < 350 km 400 km the data transmission rate of the link
between Airplane-5 and Airplane-3 will be 52.875 Mbps.
OPTIMISATION PROBLEMS
There are two problems you should address:
1. Single-objective optimisation: Find a routing path having the maximum end-to-end data
transmission rate for
each airplane that can access any of a GS, either at Heathrow airport (LHR) (Longitude,
Latitude, Altitude) =
(51.4700° N, 0.4543° W, 81.73 feet) or Newark Liberty International Airport (EWR)
(Longitude, Latitude, Altitude) =(40.6895° N, 74.1745° W, 8.72 feet).
2. Multiple-objective optimisation: Find a routing path having the maximum end-to-end data
transmission rate and minimum end-to-end latency for each airplane that can access any of a
GS, either at Heathrow airport (Longitude, Latitude, Altitude) = (51.4700° N, 0.4543° W,
81.73 feet) or Newark Liberty International Airport (Longitude, Latitude, Altitude) =
(40.6895° N, 74.1745° W, 8.72 feet).
REQUIREMENTS
Your implementation should be in Python. You are allowed to use existing Python
optimisation libraries or implementations if you need to, but you should aim to implement as
much as possible from scratch by yourself. If there is novelty/contribution of the optimisation
algorithm, it will help you to get a higher mark. You must apply your implementations to the
two routing path optimisation problems and critically evaluate the results, plotting the results
in figures, and comparing the performance, strengths, and weaknesses of the approaches you
have used in terms of quality of the solution, running time, etc.
DATASET
The dataset for this assignment consists of one file: NA_11_Jun_29_2018_UTC11.CSV
The NA_11_Jun_29_2018_UTC11.csv file contains the following columns:
1st column: Flight No. – such as AA101, AA109.
2nd column: Timestamp, which is UTC time 13:00 of Jun 29th, 2018.
3rd column: Altitude in a unit of feet.
4th column: Latitude in a unit of degree.
5th column: Longitude in a unit of degree
Note that to calculate a 3D straight distance from latitude, longitude and altitude, you will
first need to convert your points to 3D cartesian coordinates.
SOLUTION FORMAT
The solutions file contains a list of routing paths and the value of the cost function in terms of
the optimized objective.
An example journey is given below (Here is just an example, not a real optimized routing
path):
{‘AA101’, ‘rouEng path’: (AA113, 43.505), (AA51, 93.854), (LH421, 43.505), (LHR,93.854),
End-to-end data rate: ’43.505’}
where interpretation is as follows:
AA101: is the source airplane
(AA103, 43.505): The next relay node is AA103, the data transmission rate between AA101
and AA103 is 43.505 Mbps.
(AA51, 93.854): The next relay node is AA51, the data transmission rate between AA103 and
AA51 is 93.854 Mbps.
End-to-end data rate: ‘43.505’: the final end-to-end data rate is 43.505 Mbps.
SUBMISSION FORMAT
Your submission must consist of:
1. Report in the shape of a Jupyter notebook, that contains the following sections: Front matter,
Problem definition, Methodology (all steps), Experiments & discussion, Conclusion, Future
work and References. The report must be a combination of text and working code, relevant
figures (e.g. evolution of the objective function values over time), tables and anything else you
deem useful in communicating your work (e.g. interactive visualisations or animations). You
must make sure that your notebook executes from top to bottom without any intervention.
2. PDF version of your Jupyter notebook. This can be produced by simply printing your
notebook to a .pdf file. The feedback will be provided via Turnitin on this document.
3. Solution files representing your best solutions to the two optimisation problems. The files
should
follow the format given in the section “Solution format”.
