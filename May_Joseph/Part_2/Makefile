# Target executable
TARGET = customhash

# Source Python script
SOURCE = customhash.py

# Default target
all: $(TARGET)

# Rule to create the executable
$(TARGET): $(SOURCE)
	@echo "Creating executable $@ from $<"
	@cp $< $@
	@chmod +x $@

# Phony target to clean up
.PHONY: clean
clean:
	@echo "Removing $(TARGET)"
	@rm -f $(TARGET)

# Phony target to force rebuild
.PHONY: rebuild
rebuild: clean all