# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/anton/code/ss22/practicum/baselines/dense_depth_priors_nerf/preprocessing

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/anton/code/ss22/practicum/baselines/dense_depth_priors_nerf/preprocessing/build

# Include any dependencies generated for this target.
include camera/CMakeFiles/camera.dir/depend.make

# Include the progress variables for this target.
include camera/CMakeFiles/camera.dir/progress.make

# Include the compile flags for this target's objects.
include camera/CMakeFiles/camera.dir/flags.make

camera/CMakeFiles/camera.dir/src/camera.cpp.o: camera/CMakeFiles/camera.dir/flags.make
camera/CMakeFiles/camera.dir/src/camera.cpp.o: ../camera/src/camera.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/anton/code/ss22/practicum/baselines/dense_depth_priors_nerf/preprocessing/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object camera/CMakeFiles/camera.dir/src/camera.cpp.o"
	cd /home/anton/code/ss22/practicum/baselines/dense_depth_priors_nerf/preprocessing/build/camera && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/camera.dir/src/camera.cpp.o -c /home/anton/code/ss22/practicum/baselines/dense_depth_priors_nerf/preprocessing/camera/src/camera.cpp

camera/CMakeFiles/camera.dir/src/camera.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/camera.dir/src/camera.cpp.i"
	cd /home/anton/code/ss22/practicum/baselines/dense_depth_priors_nerf/preprocessing/build/camera && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/anton/code/ss22/practicum/baselines/dense_depth_priors_nerf/preprocessing/camera/src/camera.cpp > CMakeFiles/camera.dir/src/camera.cpp.i

camera/CMakeFiles/camera.dir/src/camera.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/camera.dir/src/camera.cpp.s"
	cd /home/anton/code/ss22/practicum/baselines/dense_depth_priors_nerf/preprocessing/build/camera && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/anton/code/ss22/practicum/baselines/dense_depth_priors_nerf/preprocessing/camera/src/camera.cpp -o CMakeFiles/camera.dir/src/camera.cpp.s

# Object files for target camera
camera_OBJECTS = \
"CMakeFiles/camera.dir/src/camera.cpp.o"

# External object files for target camera
camera_EXTERNAL_OBJECTS =

camera/libcamera.a: camera/CMakeFiles/camera.dir/src/camera.cpp.o
camera/libcamera.a: camera/CMakeFiles/camera.dir/build.make
camera/libcamera.a: camera/CMakeFiles/camera.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/anton/code/ss22/practicum/baselines/dense_depth_priors_nerf/preprocessing/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX static library libcamera.a"
	cd /home/anton/code/ss22/practicum/baselines/dense_depth_priors_nerf/preprocessing/build/camera && $(CMAKE_COMMAND) -P CMakeFiles/camera.dir/cmake_clean_target.cmake
	cd /home/anton/code/ss22/practicum/baselines/dense_depth_priors_nerf/preprocessing/build/camera && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/camera.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
camera/CMakeFiles/camera.dir/build: camera/libcamera.a

.PHONY : camera/CMakeFiles/camera.dir/build

camera/CMakeFiles/camera.dir/clean:
	cd /home/anton/code/ss22/practicum/baselines/dense_depth_priors_nerf/preprocessing/build/camera && $(CMAKE_COMMAND) -P CMakeFiles/camera.dir/cmake_clean.cmake
.PHONY : camera/CMakeFiles/camera.dir/clean

camera/CMakeFiles/camera.dir/depend:
	cd /home/anton/code/ss22/practicum/baselines/dense_depth_priors_nerf/preprocessing/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/anton/code/ss22/practicum/baselines/dense_depth_priors_nerf/preprocessing /home/anton/code/ss22/practicum/baselines/dense_depth_priors_nerf/preprocessing/camera /home/anton/code/ss22/practicum/baselines/dense_depth_priors_nerf/preprocessing/build /home/anton/code/ss22/practicum/baselines/dense_depth_priors_nerf/preprocessing/build/camera /home/anton/code/ss22/practicum/baselines/dense_depth_priors_nerf/preprocessing/build/camera/CMakeFiles/camera.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : camera/CMakeFiles/camera.dir/depend

