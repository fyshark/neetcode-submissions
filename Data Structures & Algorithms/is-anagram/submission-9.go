func isAnagram(s string, t string) bool {
    s_map := make(map[rune]int, 0)

    if len(s) != len(t) {
        return false
    }

    for _, sChar := range s {
        s_map[sChar] ++
    }

    for _, tChar := range t {
        s_map[tChar] --
    }

    for _, v := range s_map {
        if v != 0 {
            return false
        }
    }

    return true
}
