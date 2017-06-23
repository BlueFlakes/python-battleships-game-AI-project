import csv


class HallOfFame:
    """
    Class contains multiple methods.
    """
    @classmethod
    def print_highscore(cls, filename):
        """
        Reads .csv file and displays it correctly.

        Parameters
        ----------
        filename: csv filename
            name of the csv file

        Returns
        ----------
        None
        """

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
        """
        Saves winner's data to .csv file

        Parameters
        ----------
        filename: csv filename
            name of the csv file

        name: string
            contain winner player name

        counted_shots: int
            contain shots of winner player

        Returns
        ----------
        None
        """

        with open(filename, "a") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow([name, counted_shots])

    @classmethod
    def sort_highscore(cls, highscore):
        """
        Sorts highscore in increasing order.

        Parameters
        ----------
        highscore: list of lists
            list contain lists wit name and counted shots of winner players

        Returns
        ----------
        None
        """

        highscore.sort(key=lambda score: score[1])
