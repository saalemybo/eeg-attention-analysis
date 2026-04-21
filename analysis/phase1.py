import mne

# Load one baseline file
raw_rest = mne.io.read_raw_edf("../data/Subject00_1.edf", preload=True)

# Load one task file
raw_task = mne.io.read_raw_edf("../data/Subject00_2.edf", preload=True)

print(raw_rest)
print(raw_task)

print("Channels:", raw_rest.ch_names)
print("Sampling rate:", raw_rest.info["sfreq"])

# Quick look at a few seconds of signal
raw_rest.plot(duration=5, n_channels=10)
raw_task.plot(duration=5, n_channels=10)