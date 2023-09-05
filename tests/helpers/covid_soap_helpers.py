def get_overal_cases(xml_tree) -> int:
    return int(xml_tree.xpath("//data/summary/total_cases")[0].text)
