import MultiArmedBandit

# A few example cases that show the difference between the greedy and epsilon greedy models
MultiArmedBandit.multiArmedBandit(10, 0, 2000)
MultiArmedBandit.multiArmedBandit(10, 0.1, 2000)
MultiArmedBandit.multiArmedBandit(10, 0.01, 2000)
