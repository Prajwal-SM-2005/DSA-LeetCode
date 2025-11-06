void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    int i = m - 1;             // Pointer for nums1's last valid element
    int j = n - 1;             // Pointer for nums2's last element
    int k = m + n - 1;         // Pointer for last position in nums1

    while (i >= 0 && j >= 0) {
        if (nums1[i] > nums2[j]) {
            nums1[k--] = nums1[i--];
        } else {
            nums1[k--] = nums2[j--];
        }
    }

    // Copy remaining nums2 elements (if any)
    while (j >= 0) {
        nums1[k--] = nums2[j--];
    }
}
