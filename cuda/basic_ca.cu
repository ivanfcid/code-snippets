#include <cstdio>
#include <cuda_runtime.h>

#define W 10
#define H 10
#define STEPS 10

__global__ void step(int* in, int* out) {
    int x = blockIdx.x * blockDim.x + threadIdx.x;
    int y = blockIdx.y * blockDim.y + threadIdx.y;

    if (x >= W || y >= H) return;

    int n = 0;

    for (int dy = -1; dy <= 1; dy++)
        for (int dx = -1; dx <= 1; dx++)
            if (dx || dy)
                n += in[((y + dy + H) % H) * W + ((x + dx + W) % W)];

    int self = in[y * W + x];

    out[y * W + x] = (self && (n == 2 || n == 3)) || (!self && n == 3);
}

int main() {
    int h[W * H] = {0};

    h[(H/2)*W + W/2] = 1;
    h[(H/2)*W + W/2+1] = 1;
    h[(H/2)*W + W/2-1] = 1;

    int *a, *b;
    cudaMalloc(&a, W * H * sizeof(int));
    cudaMalloc(&b, W * H * sizeof(int));

    cudaMemcpy(a, h, W * H * sizeof(int), cudaMemcpyHostToDevice);

    dim3 threads(16,16);
    dim3 blocks((W+15)/16,(H+15)/16);

    for(int t=0;t<STEPS;t++){
        step<<<blocks,threads>>>(a,b);
        cudaMemcpy(h,b,W*H*sizeof(int),cudaMemcpyDeviceToHost);

        for(int y=0;y<H;y++){
            for(int x=0;x<W;x++)
                printf(h[y*W+x]?"#":" ");
            printf("\n");
        }
        printf("\n");

        int* tmp=a; a=b; b=tmp;
    }

    cudaFree(a);
    cudaFree(b);
}