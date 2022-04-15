# baraqda-lib
dev
Library to generate fake data reflects real data.

State: PoC

Library take counter(how much data should be generated) and language(specifies folder in wchich data should be written).
After invocating func `generate()`, data are reading to `_data` and `weights`. In next step the data is randomized
and added to variable `_draw`. This end the  process of randomization and return List of generated data.
We can also invocating function `stored_draw()` which returns data from last draw.

# How to run

After downloading folder, install libraries from requirements.txt
> pip install -r requirements.txt

Run example.py
> python3 example.py

