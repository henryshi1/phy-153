# Henry Shi
# L4ex6.py

# table of Fahrenheit values
temps_in_F = [38.0, 34.5, 29.9, 28.6, 35.1, 37.3, 29.7, 32.5,
                     27.9, 36.5, 37.5, 40.9, 31.3, 24.7, 27.5, 39.9,
                     33.6, 31.3, 33.9, 40.0, 32.2, 30.5, 37.5, 25.6,
                     36.3, 35.7, 34.9, 41.4, 37.4, 29.5, 32.3, 34.1];
temps_in_C = [];        # initialize a blank table of Celsius values

for temp in temps_in_F:          # Take each F temperature and convert to C
    temps_in_C.append( (temp-32) * 5/9 );

print(temps_in_C);       # Print the resulting C temperatures

