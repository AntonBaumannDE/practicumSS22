import torch
import torchvision.transforms.functional as TF
from PIL import Image



def eval(): 
    # compute color metrics for one generated image
    img_name = "2_rgb.jpg"
    img_path = "/home/anton/code/ss22/practicum/baselines/dense_depth_priors_nerf/experiments/11052022/20220511_230114_scene0710_00/test_images_scene0710_00/" + img_name
    pred = Image.open(img_path)
    gt_name = "949.jpg"
    gt_path = "/home/anton/code/ss22/practicum/baselines/dense_depth_priors_nerf/data_samples/scene0710_00/test/rgb/" + gt_name
    gt = Image.open(gt_path)
    x = TF.to_tensor(pred)
    y = TF.to_tensor(gt)
    mse = torch.mean((x - y) ** 2)
    print("MSE: {}".format(mse))
    psnr = -10. * torch.log(mse) / torch.log(torch.full((1,), 10., device=mse.device))
    print("PSNR: {}".format(psnr))
    #ssim = TF.ssim(x, y, data_range=x.max() - x.min())
    #print("SSIM: {}".format(ssim))
    #lpips = TF.lpips(x.permute(2,0,1).unsqueeze(0), y.permute(2,0,1).unsqueeze(0))
    #print("LPIPS: {}".format(lpips))
    return

if __name__ =='__main__': 
    eval()
