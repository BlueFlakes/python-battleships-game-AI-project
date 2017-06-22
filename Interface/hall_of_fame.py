import csv


class HallOfFame:
    @classmethod
    def print_highscore(cls, filename):
        with open(filename, "r") as f:
            highscore = f.readlines()
        for i in range(len(highscore)):
            highscore[i] = highscore[i].split(",")
            highscore[i][1] = int(highscore[i][1].strip())

        cls.sort_highscore(highscore)
        try:
            counter = 1
            for i in range(10):
                print("{}. Name: {} Shots: {}".format(counter, highscore[i][0], highscore[i][1]))
                counter += 1
        except IndexError:
            pass

    @classmethod
    def save_to_file(cls, filename, name, counted_shots):
        with open(filename, "a") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow([name, counted_shots])

    @classmethod
    def sort_highscore(cls, highscore):
        highscore.sort(key=lambda score: score[1])
