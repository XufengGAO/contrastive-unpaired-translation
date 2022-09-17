from .tmux_launcher import Options, TmuxLauncher


class Launcher(TmuxLauncher):
    def common_options(self):
        return [
            # Command 0
            Options(
                dataroot="/home/xugao/gitRepo/swapping-autoencoder-pytorch/datasets/nightVisionDatasets/",
                name="nightVision_CUT",
                CUT_mode="CUT",
                display_env="CUT",
                tb_folder="./runs/CUT/",
                epoch_count=86
            ),
            # Command 1
            Options(
                dataroot="/home/xugao/gitRepo/swapping-autoencoder-pytorch/datasets/nightVisionDatasets/",
                name="nightVision_FastCUT",
                CUT_mode="FastCUT",
                display_env="FastCUT",
                tb_folder="./runs/FastCUT/",
                epoch_count=26
            )
        ]
    
    def commands(self):
        return ["python train.py " + str(opt) for opt in self.common_options()]


    def test_commands(self):
        return ["python test.py " + str(opt.set(phase='train')) for opt in self.common_options()]