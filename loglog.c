#include "loglog.h"

int main(int argc, char ** argv) {

  FILE *fp;
  char buffer [100] = "";
  uint32_t k = 12;

  if ((fp = fopen(*++argv, "r")) == NULL) { 
    fp = stdin; 
  }

  u_int32_t size = 1 << k;
  u_int32_t M[size];

  uint32_t i;
  for (i = 0; i < size; i++) {
    M[i] = 0;
  }

  uint32_t * hash = (uint32_t *) malloc(sizeof(uint32_t));
  while ((fscanf(fp, "%100s", buffer)) == 1) {
    MurmurHash3_x86_32((void *) buffer, strlen(buffer), 42, (void *) hash);
    uint32_t index = *hash >> (32 - k);
    uint32_t rank = leadingZeroCount((*hash << k) >> k) - k + 1;
    if (rank > M[index])
      M[index] = rank;
  }

  free(hash);
  fclose(fp);

  double alphaM = 0.0;
  switch (size) {
  case 16:
    alphaM = 0.673;
    break;
  case 32:
    alphaM = 0.697;
    break;
  case 64:
    alphaM = 0.709;
    break;
  default:
    alphaM = 0.7213/(1.0 + 1.079/(double) size);
    break;
  }
  
  double sum = 0.0;
  for (i = 0; i < size; i++) {
    sum = sum + 1.0/pow(2, (double) M[i]);
  }

  double max = pow(2, 32);
  double estimate = alphaM * pow(sum, -1) * pow(size, 2);
  uint32_t * intEstimate = (uint32_t *) &estimate;

  if (estimate <= 2.5 * size) {
    double oneBits = (double) hammingDistance(*intEstimate);
    if (oneBits != 0.0) {
      estimate = size * log(size/oneBits);
    }
  }

  if (estimate <= (1.0/3.0) * max) {
    estimate = estimate;
  }
  else if (estimate > (1.0/3.0) * max) {
    estimate = (-1.0 * max) * log(1.0 - estimate/max);
  }

  printf("%lf\n", estimate);
  return 1;
}
