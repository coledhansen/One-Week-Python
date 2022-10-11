# variables that are declared in a loop are not scoped to that code block
for char in "OCTOPUS":
    color = "magenta"
    print(char)

print("AFTER LOOP: ", color) # works!

if True:
    animal = 'Osprey'

print("AFTER CONDITIONAL: ", animal)
print(char)
