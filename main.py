import ssl
import data_loader

ssl._create_default_https_context = ssl._create_unverified_context

# Miro: https://miro.com/app/board/o9J_lhf0WP8=/
if __name__ == '__main__':

    data_loader.load_data()
