# make sure you're logged in with `huggingface-cli login`
from diffusers import StableDiffusionPipeline
import platform

print(platform.platform())
# Linux-5.10.124-linuxkit-aarch64-with-glibc2.35

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", use_auth_token=True)
pipe = pipe.to("cpu")

prompt = "a photo of an astronaut riding a horse on mars"

# First-time "warmup" pass (see explanation above)
_ = pipe(prompt, num_inference_steps=1)

# Results match those from the CPU device after the warmup pass.
image_pipeline = pipe(prompt)

image = image_pipeline["sample"][0]

image.save(f"astronaut_rides_horse.png")
