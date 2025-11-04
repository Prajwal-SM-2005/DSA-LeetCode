bool isPalindrome(int x) {
    // Negative numbers are not palindrome
    if (x < 0 || (x % 10 == 0 && x != 0))
        return false;

    int reversedHalf = 0;
    while (x > reversedHalf) {
        reversedHalf = reversedHalf * 10 + x % 10;
        x /= 10;
    }

    // For even-length numbers, x == reversedHalf
    // For odd-length, x == reversedHalf/10 (middle digit ignored)
    return (x == reversedHalf || x == reversedHalf / 10);
}
