# Stable diffusion in Apple Silicon
[How to use Stable Diffusion in Apple Silicon (M1/M2)](https://huggingface.co/docs/diffusers/optimization/mps)

Blogs:
- https://huggingface.co/blog/stable_diffusion
- https://huggingface.co/blog/diffusers-2nd-month


Created a Dockerfile as the `huggingface/transformers-cpu:4.18.0` did not work.

--- image does not work on mac Apple Sillicon ---
Docker hub: https://hub.docker.com/r/huggingface/transformers-cpu > Overview

- https://docs.docker.com/desktop/mac/apple-silicon/#known-issues 
> You can add --platform linux/amd64 to run (or build) an Intel image using emulation.
> However, attempts to run Intel-based containers on Apple silicon machines under emulation can crash as qemu sometimes fails to run the container.

-------


Ue the Bash Terminal https://huggingface.co/welcome
```
huggingface-cli login
```
