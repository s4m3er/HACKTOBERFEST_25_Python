import json
import os
from datetime import datetime, timedelta

TODO_FILE = "todo_list.json"

class TodoList:
    def __init__(self):
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from JSON file"""
        if os.path.exists(TODO_FILE):
            try:
                with open(TODO_FILE, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                return []
        return []
    
    def save_tasks(self):
        """Save tasks to JSON file"""
        with open(TODO_FILE, 'w') as file:
            json.dump(self.tasks, file, indent=2)
    
    def add_task(self, description, priority="Medium", due_date=None, category="General"):
        """Add a new task to the todo list"""
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'priority': priority,
            'category': category,
            'due_date': due_date,
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✅ Task added successfully (ID: {task['id']})")
    
    def view_tasks(self, filter_type="all", category=None):
        """View tasks with optional filtering"""
        filtered_tasks = self.tasks.copy()
        
        # Apply filters
        if filter_type == "completed":
            filtered_tasks = [task for task in filtered_tasks if task['completed']]
        elif filter_type == "pending":
            filtered_tasks = [task for task in filtered_tasks if not task['completed']]
        
        if category:
            filtered_tasks = [task for task in filtered_tasks if task['category'].lower() == category.lower()]
        
        if not filtered_tasks:
            print("No tasks found.")
            return
        
        print(f"\n{'='*80}")
        print(f"{'TO-DO LIST':^80}")
        print(f"{'='*80}")
        print(f"{'ID':<4} {'Status':<12} {'Priority':<10} {'Category':<12} {'Due Date':<12} {'Description'}")
        print(f"{'-'*80}")
        
        for task in filtered_tasks:
            status = "✅ Done" if task['completed'] else "⏳ Pending"
            priority_icon = {
                "High": "🔴",
                "Medium": "🟡", 
                "Low": "🟢"
            }.get(task['priority'], "⚪")
            
            due_date = task['due_date'] if task['due_date'] else "No due date"
            
            print(f"{task['id']:<4} {status:<12} {priority_icon} {task['priority']:<8} {task['category']:<12} {due_date:<12} {task['description']}")
        
        print(f"{'='*80}")
        print(f"Total tasks: {len(filtered_tasks)}")
    
    def mark_completed(self, task_id):
        """Mark a task as completed"""
        for task in self.tasks:
            if task['id'] == task_id:
                if not task['completed']:
                    task['completed'] = True
                    task['completed_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    self.save_tasks()
                    print(f"✅ Task {task_id} marked as completed!")
                else:
                    print(f"ℹ️ Task {task_id} is already completed.")
                return
        print(f"❌ Task with ID {task_id} not found.")
    
    def mark_pending(self, task_id):
        """Mark a completed task as pending again"""
        for task in self.tasks:
            if task['id'] == task_id:
                if task['completed']:
                    task['completed'] = False
                    if 'completed_at' in task:
                        del task['completed_at']
                    self.save_tasks()
                    print(f"🔄 Task {task_id} marked as pending again!")
                else:
                    print(f"ℹ️ Task {task_id} is already pending.")
                return
        print(f"❌ Task with ID {task_id} not found.")
    
    def delete_task(self, task_id):
        """Delete a task from the list"""
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                deleted_task = self.tasks.pop(i)
                self.save_tasks()
                # Reassign IDs to maintain sequence
                for j, task in enumerate(self.tasks, 1):
                    task['id'] = j
                self.save_tasks()
                print(f"🗑️ Task '{deleted_task['description']}' deleted successfully!")
                return
        print(f"❌ Task with ID {task_id} not found.")
    
    def edit_task(self, task_id, new_description=None, new_priority=None, new_category=None, new_due_date=None):
        """Edit an existing task"""
        for task in self.tasks:
            if task['id'] == task_id:
                if new_description:
                    task['description'] = new_description
                if new_priority:
                    task['priority'] = new_priority
                if new_category:
                    task['category'] = new_category
                if new_due_date:
                    task['due_date'] = new_due_date
                
                self.save_tasks()
                print(f"✏️ Task {task_id} updated successfully!")
                return
        print(f"❌ Task with ID {task_id} not found.")
    
    def get_statistics(self):
        """Display statistics about tasks"""
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task['completed'])
        pending_tasks = total_tasks - completed_tasks
        
        print(f"\n{'📊 TASK STATISTICS':^50}")
        print(f"{'='*50}")
        print(f"Total tasks: {total_tasks}")
        print(f"Completed: {completed_tasks}")
        print(f"Pending: {pending_tasks}")
        
        if total_tasks > 0:
            completion_rate = (completed_tasks / total_tasks) * 100
            print(f"Completion rate: {completion_rate:.1f}%")
        
        # Tasks by priority
        priorities = {}
        categories = {}
        for task in self.tasks:
            priorities[task['priority']] = priorities.get(task['priority'], 0) + 1
            categories[task['category']] = categories.get(task['category'], 0) + 1
        
        print(f"\nBy Priority:")
        for priority, count in priorities.items():
            print(f"  {priority}: {count}")
        
        print(f"\nBy Category:")
        for category, count in categories.items():
            print(f"  {category}: {count}")
    
    def clear_completed(self):
        """Remove all completed tasks"""
        completed_count = sum(1 for task in self.tasks if task['completed'])
        if completed_count == 0:
            print("ℹ️ No completed tasks to clear.")
            return
        
        self.tasks = [task for task in self.tasks if not task['completed']]
        
        # Reassign IDs
        for i, task in enumerate(self.tasks, 1):
            task['id'] = i
        
        self.save_tasks()
        print(f"🧹 Cleared {completed_count} completed tasks!")

def get_due_date_input():
    """Helper function to get due date from user"""
    print("\nDue date options:")
    print("1. Today")
    print("2. Tomorrow") 
    print("3. Next week")
    print("4. Custom date")
    print("5. No due date")
    
    choice = input("Choose option (1-5): ").strip()
    
    if choice == "1":
        return datetime.now().strftime("%Y-%m-%d")
    elif choice == "2":
        return (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    elif choice == "3":
        return (datetime.now() + timedelta(weeks=1)).strftime("%Y-%m-%d")
    elif choice == "4":
        date_str = input("Enter due date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("❌ Invalid date format. Using no due date.")
            return None
    else:
        return None

def main():
    todo_list = TodoList()
    
    print("🎯 WELCOME TO YOUR TO-DO LIST MANAGER")
    print("=" * 50)
    
    while True:
        print("\n📋 MAIN MENU:")
        print("1. ➕ Add new task")
        print("2. 👀 View tasks")
        print("3. ✅ Mark task as completed")
        print("4. 🔄 Mark task as pending")
        print("5. ✏️ Edit task")
        print("6. 🗑️ Delete task")
        print("7. 📊 Show statistics")
        print("8. 🧹 Clear completed tasks")
        print("9. ❌ Exit")
        
        choice = input("\nEnter your choice (1-9): ").strip()
        
        if choice == "1":
            print("\n➕ ADD NEW TASK")
            description = input("Enter task description: ").strip()
            if not description:
                print("❌ Task description cannot be empty!")
                continue
            
            print("\nPriority levels:")
            print("1. 🔴 High")
            print("2. 🟡 Medium") 
            print("3. 🟢 Low")
            priority_choice = input("Choose priority (1-3, default 2): ").strip()
            priority = {"1": "High", "2": "Medium", "3": "Low"}.get(priority_choice, "Medium")
            
            category = input("Enter category (default: General): ").strip()
            category = category if category else "General"
            
            due_date = get_due_date_input()
            
            todo_list.add_task(description, priority, due_date, category)
        
        elif choice == "2":
            print("\n👀 VIEW TASKS")
            print("1. All tasks")
            print("2. Pending tasks")
            print("3. Completed tasks")
            print("4. Tasks by category")
            view_choice = input("Choose view option (1-4): ").strip()
            
            if view_choice == "1":
                todo_list.view_tasks("all")
            elif view_choice == "2":
                todo_list.view_tasks("pending")
            elif view_choice == "3":
                todo_list.view_tasks("completed")
            elif view_choice == "4":
                category = input("Enter category name: ").strip()
                todo_list.view_tasks("all", category)
            else:
                todo_list.view_tasks("all")
        
        elif choice == "3":
            todo_list.view_tasks("pending")
            try:
                task_id = int(input("\nEnter task ID to mark as completed: "))
                todo_list.mark_completed(task_id)
            except ValueError:
                print("❌ Please enter a valid task ID!")
        
        elif choice == "4":
            todo_list.view_tasks("completed")
            try:
                task_id = int(input("\nEnter task ID to mark as pending: "))
                todo_list.mark_p
