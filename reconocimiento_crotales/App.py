from reconocimiento_crotales.PretrainedReader import PretrainedReader
import fire


class App:
    def process_image(self, path):
        reader = PretrainedReader()
        identifier = reader.process_image(path)
        return identifier.get_value()


if __name__ == '__main__':
    fire.Fire(App)
