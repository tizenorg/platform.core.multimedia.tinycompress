CMAKE_MINIMUM_REQUIRED(VERSION 2.6)
PROJECT(tinycompress C)

#INCLUDE(FindPkgConfig)

SET(PREFIX ${CMAKE_INSTALL_PREFIX})
SET(EXEC_PREFIX "\${prefix}")
SET(LIBDIR "\${prefix}/lib")
SET(INCLUDEDIR "\${prefix}/include")

# Set required packages
INCLUDE(FindPkgConfig)
pkg_check_modules(pkgs REQUIRED alsa)

FOREACH(flag ${pkgs_CFLAGS})
	SET(EXTRA_CFLAGS "${EXTRA_CFLAGS} ${flag}")
ENDFOREACH(flag)

SET(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -I${CMAKE_SOURCE_DIR}/include ${EXTRA_CFLAGS} -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -Wdeclaration-after-statement -Wmissing-declarations -Wredundant-decls -Wcast-align")

MESSAGE(${CMAKE_C_FLAGS})
MESSAGE(${CMAKE_EXE_LINKER_FLAGS})

SET(CPLAY_SRCS
		cplay.c
)

SET(TINYCOMPRESS_SRCS
		compress.c
		utils.c
)

# library build
ADD_LIBRARY(tinycompress SHARED ${TINYCOMPRESS_SRCS})
TARGET_LINK_LIBRARIES(tinycompress ${pkgs_LDFLAGS})
SET_TARGET_PROPERTIES(tinycompress PROPERTIES VERSION 0.1.0 SOVERSION 0 OUTPUT_NAME tinycompress)

# executable build
ADD_EXECUTABLE(cplay ${CPLAY_SRCS})
TARGET_LINK_LIBRARIES(cplay ${pkg_LDFLAGS} tinycompress)

# pkgconfig file
SET(PREFIX ${CMAKE_INSTALL_PREFIX})
CONFIGURE_FILE(tinycompress.pc.in tinycompress.pc @ONLY)


# install
INSTALL(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/ DESTINATION include/tinycompress-0.2.0)
INSTALL(TARGETS tinycompress LIBRARY DESTINATION lib)
INSTALL(TARGETS cplay RUNTIME DESTINATION bin)
INSTALL(FILES ${CMAKE_CURRENT_BINARY_DIR}/tinycompress.pc DESTINATION lib/pkgconfig)
