import { Component, OnInit } from '@angular/core';

import { Task } from '../model/task';
import { TaskService } from '../model/task.service';

@Component({
    selector: 'tasks',
    templateUrl: 'app/tasks/tasks.component.html'
})
export class TasksComponent {
    constructor(
        private taskService: TaskService
    ) {}

    private tasks: Task[]

    ngOnInit() {
        this.refresh()
    }

	addTask(): void {
        console.log('addTask');
    }

    refresh(): void {
        this.taskService.getTasks().then((tasks) => this.tasks = tasks);
    }
}