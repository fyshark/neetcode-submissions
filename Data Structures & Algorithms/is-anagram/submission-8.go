func isAnagram(s string, t string) bool {
    s_map := make(map[rune]int, 0)
    t_map := make(map[rune]int, 0)

    if len(s) != len(t) {
        return false
    }

    for _, sChar := range s {
        s_map[sChar] ++
    }

    for _, tChar := range t {
        t_map[tChar] ++
    }

    for k, v := range s_map {
        if t_map[k] != v {
            return false
        }
    }

    return true
}
