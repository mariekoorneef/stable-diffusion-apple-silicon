# Stable diffusion with Docker on Apple Silicon

Docs:
[How to use Stable Diffusion in Apple Silicon (M1/M2)](https://huggingface.co/docs/diffusers/optimization/mps)

Blogs:
- https://huggingface.co/blog/stable_diffusion
- https://huggingface.co/blog/diffusers-2nd-month


Untortunately the `huggingface/transformers-cpu:4.18.0` did not work.
- See [Docker Desktop for Apple silicon | known-issues](https://docs.docker.com/desktop/mac/apple-silicon/#known-issues)
> You can add --platform linux/amd64 to run (or build) an Intel image using emulation.
>
> However, attempts to run Intel-based containers on Apple silicon machines under emulation can crash as qemu sometimes fails to run the container.

---

Make sure you're logged in with
```
huggingface-cli login
```

https://huggingface.co/welcome
