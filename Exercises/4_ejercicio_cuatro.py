def costo(m,a,v):
    m_t = m * 4
    a_t = a * 5
    v_t = v * 8
    return m_t,a_t,v_t

def material_eco(m,a,v):
    m_t,a_t,v_t = costo(m, a, v)
    if m_t < a_t < v_t or m_t < v_t < a_t:
        return "Con madera sale más económico"
    elif v_t < m_t < a_t or v_t < a_t < m_t:
        return "Con varilla sale más económico"
    elif a_t < m_t < v_t or a_t < v_t < m_t:
        return "Con alambre sale más económico"
    else:
        return "Por lo menos dos materiales salen por el mismo precio."

def main():
    m = int(input("Digíte el costo del tablón de madera de un metro en pesos: "))
    a = int(input("Digíte el costo del metro de alambre de púas en pesos: "))
    v = int(input("Digíte el costo del metro de varilla en pesos: "))
    print(material_eco(m,a,v))

main()