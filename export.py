def export_csv(tasks):
    lines = ["title,done"]
    for t in tasks:
        lines.append(f"{t['title']},{t.get('done', False)}")
    return "\n".join(lines)
