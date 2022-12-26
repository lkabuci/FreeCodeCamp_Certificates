#include <stdio.h>
#include <stdlib.h>

static int	*set_array(int size, int fill)
{
	int	*arr;
	int	i;

	i = 0;
	arr = malloc(sizeof(int) * size);
	if (!arr)
		return (NULL);
	while (i < size)
	{
		arr[i] = fill;
		i++;
	}
	return (arr);
}

static void	reverse_array(int **arr, int size)
{
	int	i;

	i = 0;
	while (i < size / 2)
	{
		(*arr)[i] ^= (*arr)[size - i - 1];
		(*arr)[size - i - 1] ^= (*arr)[i];
		(*arr)[i] ^= (*arr)[size - i - 1];
		i++;
	}
}

static void	set_dup_prev(int *sequence, int **dp, int **prev, int size)
{
	int	i;
	int	j;

	i = 1;
	while (i < size)
	{
		j = 0;
		while (j < i)
		{
			if (sequence[j] < sequence[i] && (*dp)[j] + 1 > (*dp)[i])
			{
				(*dp)[i] = (*dp)[j] + 1;
				(*prev)[i] = j;
			}
			j++;
		}
		i++;
	}
}

static int	lis_len(int *dp, int size)
{
	int	i;
	int	j;

	i = 0;
	j = 1;
	while (j < size)
	{
		if (dp[j] > dp[i])
			i = j;
		j++;
	}
	printf("size of lis is: %d\n", dp[i]);
	fflush(stdout);
	return (i);
}

static int	*generate_lis(int *sequence, int *dp, int *prev, int i, int size)
{
	int	*lis;
	int	index;

	index = 0;
	lis = malloc(sizeof(int) * (size + 1));
	if (!lis)
		return (NULL);
	while (i != -1)
	{
		lis[index] = sequence[i];
		index++;
		i = prev[i];
	}
	return (reverse_array(&lis, size), lis);
}

int	*lis(int *list, int n)
{
	int	*dp;
	int	*prev;
	int	max;
	int	*sequence;

	dp = set_array(n, 1);
	prev = set_array(n, -1);
	set_dup_prev(list, &dp, &prev, n);
	max = lis_len(dp, n);
	sequence = generate_lis(list, dp, prev, max, dp[max]);
	return (free(dp), free(prev), sequence);
}

int main()
{
	int list[] = {0, 13, 18, 98, 97, 32, 56, 62, 5, 1};
	int *lisequence = lis(list, sizeof(list) / sizeof(int));
	for (int i = 0; i < 6; i++)
		printf("%d, ", lisequence[i]);
	printf("\n");
	free(lisequence);
	return (0);
}
