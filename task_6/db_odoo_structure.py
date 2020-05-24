class project_student(model.Models()):
    _name = 'project.student'

    surname = fields.Char()
    name = fields.Char()
    middle_name = fields.Char()
    birthdate = fields.Datetime()
    birthplace_id = fields.Many2one('project.birthplace')
    group_id = fields.Many2one('project.group')
    is_studying = fields.Boolean()


class project_group(model.Models()):
    _name = 'project.group'

    group_number = fields.Integer()
    faculty = fields.Char()


class project_birthplace(model.Models()):
    _name = 'project.birthplace'

    address = fields.Char()
