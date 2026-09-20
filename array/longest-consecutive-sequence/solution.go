package main

func main() {
	longestConsecutive([]int{1, 2, 3, 2, 3, 1})
}

func longestConsecutive(nums []int) int {
	// create set
	set := make(map[int]bool)

	// populate the set
	for _, val := range nums {
		set[val] = true
	}

	longest := 0

	// the main algo
	for key := range set {
		current_longest := 0

		if set[key-1] {
			continue
		} else {
			current_longest++
			current_num := key

			for set[current_num+1] {
				current_longest++
				current_num++
			}
		}

		longest = max(longest, current_longest)
	}

	return longest
}
