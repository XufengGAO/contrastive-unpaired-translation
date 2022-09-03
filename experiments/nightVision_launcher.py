from .tmux_launcher import Options, TmuxLauncher


class Launcher(TmuxLauncher):
    def common_options(self):
        return [
            Options(
                dataroot="/home/xugao/gitRepo/swapping-autoencoder-pytorch/datasets/nightVisionDatasets/",
                name="nightVision_CUT_default",
                CUT_mode="CUT",
                preprocess="scale_shortside_and_crop",
                gpu_ids="0,1"
            )
        ]
    
    def commands(self):
        return ["python train.py " + str(opt) for opt in self.common_options()]


    def test_commands(self):
        return ["python test.py " + str(opt.set(phase='train')) for opt in self.common_options()]