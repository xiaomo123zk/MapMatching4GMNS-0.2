# Cross-Platform MapMatching4GMNS

This repo is an **independent development** from [asu-trans-ai-lab/MapMatching4GMNS](https://github.com/asu-trans-ai-lab/MapMatching4GMNS). It aims to provide a clean and common C++ code base (over its original implementation) to build both executable and shared library of MapMatching4GMNS across platforms.
 
The legacy source and binary files are all deprecated and moved to the [archive folder](https://github.com/xiaomo123zk/MapMatching4GMNS-master) for referrence only.

## Build MapMatching4GMNS
We use the cross-platform tool CMake to define the building process.

*Build the executable using CMake and run it on Windows system or Liunx system*
```
# from the root directory of engine (i.e., MapMatching4GMNS/engine)
$ mkdir build
$ cd build
$ cmake .. -DBUILD_EXE=ON
$ cmake --build .
```
*Build the executable using CMake and run it on Mac system*
```
# from the root directory of engine (i.e., MapMatching4GMNS/engine)
$ g++ -shared -fPIC -o MapMatching4GMNS.dylib MapMatching4GMNS.cpp
$ g++ -shared -fPIC -o MapMatching4GMNS.dylib MapMatching4GMNS.cpp
```

You can remove -DBUILD_EXE=ON or -DBUILD_EXE=OFF if you prefer to manually change the value of BUILD_EXE in [CMakeLists.txt](https://github.com/xiaomo123zk/MapMatching4GMNS/blob/main/engine/CMakeLists.txt).

*Windows Users*

A classic Visual Studio solution file is shipped as well along with the project file to **build executable only on Windows** for the convenience of users who are not familar with CMake. **Note that** they are not built on CMakeLists.txt. If you are planning to build the shared library of MapMatching4GMNS, there are three ways to do it as shown below.

1. Let CMake automatically generate solution and project files for you by using the commands above. It is the easiest and recommmended way;
2. [Create your own Visual Studio project](https://docs.microsoft.com/en-us/visualstudio/get-started/tutorial-projects-solutions?view=vs-2019) under the shipped solution;
3. [Create new CMake projects in Visual Studio](https://docs.microsoft.com/en-us/cpp/build/cmake-projects-in-visual-studio?view=msvc-160) by including the embedded [CMakeLists.txt](https://github.com/jdlph/MapMatching4GMNS/blob/main/src_cpp/src/CMakeLists.txt).


[C++ source code](https://github.com/xiaomo123zk/MapMatching4GMNS-master/src)
 
### Other References: 
This code is implemented partially based on a published paper in Transportation Research Part C:

Tang J, Song Y, Miller HJ, Zhou X (2015) “Estimating the most likely space–time paths, dwell times and path uncertainties from vehicle trajectory data: A time geographic method,” *Transportation Research Part C*,
<http://dx.doi.org/10.1016/j.trc.2015.08.014>