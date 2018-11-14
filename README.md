# Midterm Make up

1. Didn't get to this one in time.

2. To run the script, run `python scales.py -f <your fundamental here>`

3. For a 10hz frequency resolution that is sampled at 40k hz, we get 4000 frequency bins. This means that we get a frequency bin perfectly at 2000 hz. The file says 1khz, but the 2k hz looks to be the fundamental. The flattop minimizes the noise and gives an accurate amplitude at the peaks while the hanning window creates a side lob with a more gradual decay. For a subset of 3500 samples, we get slightly less resolution of roughly ~11.4hz per bin. This means that we won't have a bin directly on the frequency. This leads to slightly more spectral leakage which is minimized in the flatop view and accentuated in  
the hanning window representation. `python fft.py` is how you run the file that generated the graphes and applied the various windows for analysis. Running the code requires a dependencies. These are listed in `requirements.txt`. On a mac, install these requirements with `virtualenv`.
    1. Install vritualenv with pip  `pip install virtualenv`
    2. Create a virtual environment `virtualenv env`
    3. Activate the environement with `source env/bin/activate`
    4. Install dependencies within the context of the environment with `pip install -r requirements.txt`
    
4. With high acoustic impedance, the resonances that occur at those spikes are the only tones that the instrument will play. These peaks can also be considered ratios of the odd harmonics 1:3:5:7, etc.
Despite running an FFT on both the clarinet and flute files, along with trying flatop windowing, I wasn't able to ascertain peaks that well. On the clarinet, the fundamental seemed to be roughly an F. The next 5 noticeable notes would be the next six odd harmonics from the fundamental. 
