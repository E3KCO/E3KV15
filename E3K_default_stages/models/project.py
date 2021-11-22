# -*- coding: utf-8 -*-
from odoo import models, fields, api, _



class project_project(models.Model):
    _inherit = 'project.project'

    @api.model
    def _get_type_common(self):
        list = self.env['project.task.type'].search([('is_fold','=',1)])
        ids = []
        for x in list:
            ids.append(x.id)
        return ids
     
    
    type_ids = fields.Many2many('project.task.type', 'project_task_type_rel', 'project_id', 'type_id', 'Tasks Stages', 
                                
                                default=_get_type_common) 
        
    
class project_task_type(models.Model):
    _inherit = 'project.task.type'
    
    is_fold = fields.Boolean(string='Default for New Projects',
                          help="If you check this field, this stage will be proposed by default on each new project. It will not assign this stage to existing projects.")
        
