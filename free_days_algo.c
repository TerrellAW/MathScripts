#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <limits.h>
#include <getopt.h>

// Long option definitions for CLI arg parsing
struct option long_options[] = {
	{"days", required_argument, 0, 'd'},	// --days or -d
	{"one", required_argument, 0, 'o'},		// --one or -o
	{"three", required_argument, 0, 't'}	// --three or -t
};

/**
 * Rounds a double up to the nearest integer (ceiling function).
 * Handles overflow by capping at INT_MAX.
 * 
 * @param dbl The double value to round up
 * @return The ceiling as an integer
 */
int ceiling(double dbl) {
	// Check for overflow - if value exceeds int range, return max
	if (dbl >= INT_MAX) {
		return INT_MAX;
	}

	// Cast to int (truncates decimal portion)
	int num = (int) dbl;

	// If there was a fractional part, round up
	if (dbl > num) {
		return num + 1;
	} else {
		return num;
	}
}

/**
 * Calculates how many weeks are needed to complete a task given
 * variable weekly availability.
 * 
 * @param task_days_needed Total days required for the task
 * @param one_per_week_pct Percentage of weeks with 1 day available (0-1)
 * @param three_per_week_pct Percentage of weeks with 3 days available (0-1)
 * @return Number of weeks needed, or -1 on error
 */
int calculateTaskWeeks(int task_days_needed, double one_per_week_pct, double three_per_week_pct) {
	double two_per_week_pct;
	double one_three_pct = one_per_week_pct + three_per_week_pct;
	
	// Validate that percentages are in valid range and sum to <= 1
	if (one_three_pct > 1 || one_three_pct <= 0) {
		fprintf(stderr, "Invalid percentage: %f\n", one_three_pct);
		return -1;
	} else {
		// Calculate remaining percentage for 2 days/week
   		two_per_week_pct = 1 - one_three_pct;
	}

	// Calculate weighted average days available per week
	double avg = (1 * one_per_week_pct) + (2 * two_per_week_pct) + (3 * three_per_week_pct);

	// Calculate weeks needed and round up
	double weeks = task_days_needed / avg;
	int weeks_needed = ceiling(weeks);
	return weeks_needed;
}

int main(int argc, char *argv[]) {
	// Default values
	int task_days = 20;
	double one_per_week = 0.25;
	double three_per_week = 0.25;

	// Parse args
	int opt;
	while ((opt = getopt_long(argc, argv, "d:o:t:", long_options, NULL)) != -1) {
		switch (opt) {
			case 'd':
				task_days = atoi(optarg);
				break;
			case 'o':
				one_per_week = atof(optarg);
				break;
			case 't':
				three_per_week = atof(optarg);
				break;
		}
	}

	// Validate task_days
	if (task_days <= 0) {
		fprintf(stderr, "Invalid amount of days: %d\n", task_days);
		exit(EXIT_FAILURE);
	}

	// Calculate weeks needed to complete task
	int weeks = calculateTaskWeeks(task_days, one_per_week, three_per_week);

	if (weeks == -1) {
		fprintf(stderr, "Calculation failed due to invalid inputs\n");
		exit(EXIT_FAILURE);
	}

	// Output
	printf("Task days needed: %d\n", task_days);
	printf("1 day/week: %.2f%% | 2 days/week: %.2f%% | 3 days/week: %.2f%%\n", 
			one_per_week * 100, 
			(1 - one_per_week - three_per_week) * 100,
			three_per_week * 100);
	printf("Weeks needed: %d\n", weeks);

	exit(EXIT_SUCCESS);
}
