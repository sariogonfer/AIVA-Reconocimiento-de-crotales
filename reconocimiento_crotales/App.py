from reconocimiento_crotales.PretrainedReader import PretrainedReader
import fire


class App:
    def process_image(self, path):
        reader = PretrainedReader()
        return reader.process_image(path)


if __name__ == '__main__':
    fire.Fire(App)
