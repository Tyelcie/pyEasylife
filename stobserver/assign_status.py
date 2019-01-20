def assign_status(x, student, projects, status):
    students_idx = x[x['Name'].isin([student])].index
    projects_idx = x[projects].columns
    x.loc[students_idx, projects_idx] = status
    return x
