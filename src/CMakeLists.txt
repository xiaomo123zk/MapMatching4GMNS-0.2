# CMakeList.txt: Matching2Path's CMake program 
 
cmake_minimum_required (VERSION 3.5)

project ("MapMatching4GMNS")


if(WIN32)
    message("Building dll file on Windows")
elseif(UNIX)
    message("Building so or dylib file on ${CMAKE_SYSTEM_NAME}")
endif()

set(CMAKE_CXX_STANDARD 11)


# note CMAKE_BUILD_TYPE WILL BE INGNORED for IDE generators, like Visual Studio and Xcode
# it only works for single-configuration generators, e.g., make and Ninja
# see https://cmake.org/cmake/help/v3.0/variable/CMAKE_BUILD_TYPE.html?highlight=cmake_build_types for details
set(CMAKE_BUILD_TYPE  "Release")
set(LIBRARY_OUTPUT_PATH  ${CMAKE_BINARY_DIR}/bin)

#FIND_PACKAGE( OpenMP REQUIRED)
#if(OPENMP_FOUND)
#message("OPENMP FOUND")
#set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
#set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
#set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} ${OpenMP_EXE_LINKER_FLAGS}")
#endif()

add_library(MapMatching4GMNS SHARED  MapMatching4GMNS.cpp)

#This is best known as the -fPIC flag. Much of the time, you don't need to do anything. 
#CMake will include the flag for SHARED or MODULE libraries. 
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# If you need to explicitly link to the math library, you can always do target_link_libraries(MyTarget PUBLIC m)
#find_library(MATH_LIBRARY m)
#if(MATH_LIBRARY)
#    target_link_libraries(MyTarget PUBLIC ${MATH_LIBRARY})
#endif()