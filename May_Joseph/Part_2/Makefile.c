# Compiler
CC = gcc

# Compiler Flags
CFLAGS = -Wall -g

# Target executable
TARGET = c_program

# Rule to build the target
$(TARGET): c_program.c
	$(CC) $(CFLAGS) -o $(TARGET) c_program.c

# Clean rule to remove the compiled binary
clean:
	rm -rf $(TARGET) *.dSYM
