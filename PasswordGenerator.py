import random
import string
import secrets
import argparse
import pyperclip  # For clipboard functionality
import sys
from datetime import datetime

class PasswordGenerator:
    def __init__(self):
        self.strength_levels = {
            'weak': (8, 12, False, False),
            'medium': (12, 16, True, False),
            'strong': (16, 20, True, True),
            'very-strong': (20, 25, True, True)
        }
    
    def generate_password(self, length=16, use_uppercase=True, use_lowercase=True, 
                         use_numbers=True, use_symbols=True, exclude_similar=True):
        """
        Generate a random password with specified criteria
        """
        # Character sets
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        numbers = string.digits
        symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        # Characters to exclude (similar looking)
        similar_chars = "il1Lo0O"
        
        # Build character pool
        char_pool = ""
        if use_lowercase:
            if exclude_similar:
                char_pool += ''.join(c for c in lowercase if c not in similar_chars)
            else:
                char_pool += lowercase
        if use_uppercase:
            if exclude_similar:
                char_pool += ''.join(c for c in uppercase if c not in similar_chars)
            else:
                char_pool += uppercase
        if use_numbers:
            if exclude_similar:
                char_pool += ''.join(c for c in numbers if c not in similar_chars)
            else:
                char_pool += numbers
        if use_symbols:
            char_pool += symbols
        
        # Validate character pool
        if not char_pool:
            raise ValueError("At least one character type must be selected")
        
        if len(char_pool) < length:
            raise ValueError(f"Character pool too small for password length {length}")
        
        # Generate password using cryptographically secure random generator
        password = ''.join(secrets.choice(char_pool) for _ in range(length))
        
        # Ensure at least one of each selected character type is included
        password = self._ensure_character_types(password, use_lowercase, use_uppercase, 
                                              use_numbers, use_symbols, char_pool)
        
        return password
    
    def _ensure_character_types(self, password, use_lowercase, use_uppercase, 
                              use_numbers, use_symbols, char_pool):
        """
        Ensure the password contains at least one of each selected character type
        """
        chars_to_ensure = []
        
        if use_lowercase and not any(c.islower() for c in password):
            chars_to_ensure.append(random.choice([c for c in char_pool if c.islower()]))
        if use_uppercase and not any(c.isupper() for c in password):
            chars_to_ensure.append(random.choice([c for c in char_pool if c.isupper()]))
        if use_numbers and not any(c.isdigit() for c in password):
            chars_to_ensure.append(random.choice([c for c in char_pool if c.isdigit()]))
        if use_symbols and not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
            chars_to_ensure.append(random.choice([c for c in char_pool if c in "!@#$%^&*()_+-=[]{}|;:,.<>?"]))
        
        if chars_to_ensure:
            # Replace random positions with the required characters
            password_list = list(password)
            for char in chars_to_ensure:
                pos = secrets.randbelow(len(password_list))
                password_list[pos] = char
            password = ''.join(password_list)
        
        return password
    
    def generate_from_strength(self, strength='strong'):
        """
        Generate password based on predefined strength levels
        """
        if strength not in self.strength_levels:
            raise ValueError(f"Invalid strength level. Choose from: {list(self.strength_levels.keys())}")
        
        min_len, max_len, use_symbols, exclude_similar = self.strength_levels[strength]
        length = random.randint(min_len, max_len)
        
        return self.generate_password(
            length=length,
            use_uppercase=True,
            use_lowercase=True,
            use_numbers=True,
            use_symbols=use_symbols,
            exclude_similar=exclude_similar
        )
    
    def generate_multiple(self, count=5, **kwargs):
        """
        Generate multiple passwords at once
        """
        return [self.generate_password(**kwargs) for _ in range(count)]
    
    def calculate_strength(self, password):
        """
        Calculate password strength score (0-100)
        """
        score = 0
        length = len(password)
        
        # Length score (max 30 points)
        score += min(30, length * 2)
        
        # Character variety score (max 40 points)
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_symbol = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
        
        char_types = sum([has_lower, has_upper, has_digit, has_symbol])
        score += char_types * 10  # 10 points per character type
        
        # Entropy bonus (max 30 points)
        unique_chars = len(set(password))
        entropy_bonus = min(30, (unique_chars / length) * 30)
        score += entropy_bonus
        
        return min(100, int(score))
    
    def get_strength_label(self, score):
        """
        Get strength label based on score
        """
        if score >= 90:
            return "🔒 Very Strong"
        elif score >= 75:
            return "🛡️ Strong"
        elif score >= 60:
            return "⚠️ Medium"
        elif score >= 40:
            return "🔓 Weak"
        else:
            return "💀 Very Weak"
    
    def check_common_password(self, password):
        """
        Check if password is in common passwords list
        """
        common_passwords = {
            'password', '123456', '12345678', '1234', 'qwerty', '12345',
            'dragon', 'baseball', 'football', 'letmein', 'monkey',
            'abc123', 'password1', 'admin', 'welcome', 'sunshine'
        }
        return password.lower() in common_passwords

def display_password_info(password, generator):
    """
    Display information about the generated password
    """
    strength_score = generator.calculate_strength(password)
    strength_label = generator.get_strength_label(strength_score)
    is_common = generator.check_common_password(password)
    
    print(f"\n🔐 Generated Password: {password}")
    print(f"📊 Length: {len(password)} characters")
    print(f"💪 Strength: {strength_label} ({strength_score}/100)")
    
    if is_common:
        print("⚠️  Warning: This is a commonly used password!")
    
    # Character composition
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    
    print("📝 Contains:")
    print(f"   - Lowercase letters: {'✅' if has_lower else '❌'}")
    print(f"   - Uppercase letters: {'✅' if has_upper else '❌'}")
    print(f"   - Numbers: {'✅' if has_digit else '❌'}")
    print(f"   - Symbols: {'✅' if has_symbol else '❌'}")

def interactive_mode():
    """
    Interactive mode for user-friendly password generation
    """
    generator = PasswordGenerator()
    
    print("🎯 PASSWORD GENERATOR")
    print("=" * 50)
    
    while True:
        print("\n🔧 Generation Options:")
        print("1. Quick generate (Strong password)")
        print("2. Custom password")
        print("3. Generate by strength level")
        print("4. Generate multiple passwords")
        print("5. Check password strength")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            # Quick generate
            password = generator.generate_from_strength('strong')
            display_password_info(password, generator)
            
        elif choice == "2":
            # Custom password
            try:
                length = int(input("Enter password length (8-50): ") or "16")
                use_upper = input("Include uppercase letters? (y/n): ").lower() in ['y', 'yes']
                use_lower = input("Include lowercase letters? (y/n): ").lower() in ['y', 'yes']
                use_nums = input("Include numbers? (y/n): ").lower() in ['y', 'yes']
                use_syms = input("Include symbols? (y/n): ").lower() in ['y', 'yes']
                exclude_similar = input("Exclude similar characters (i,l,1,L,o,0,O)? (y/n): ").lower() in ['y', 'yes']
                
                password = generator.generate_password(
                    length=length,
                    use_uppercase=use_upper,
                    use_lowercase=use_lower,
                    use_numbers=use_nums,
                    use_symbols=use_syms,
                    exclude_similar=exclude_similar
                )
                display_password_info(password, generator)
                
            except ValueError as e:
                print(f"❌ Error: {e}")
                
        elif choice == "3":
            # Generate by strength level
            print("\n💪 Strength Levels:")
            print("1. Weak (8-12 chars, no symbols)")
            print("2. Medium (12-16 chars, with symbols)")
            print("3. Strong (16-20 chars, with symbols, exclude similar)")
            print("4. Very Strong (20-25 chars, with symbols, exclude similar)")
            
            level_choice = input("Choose strength level (1-4): ").strip()
            levels = {'1': 'weak', '2': 'medium', '3': 'strong', '4': 'very-strong'}
            
            if level_choice in levels:
                password = generator.generate_from_strength(levels[level_choice])
                display_password_info(password, generator)
            else:
                print("❌ Invalid choice!")
                
        elif choice == "4":
            # Generate multiple passwords
            try:
                count = int(input("How many passwords to generate? (1-20): ") or "5")
                count = max(1, min(20, count))
                
                passwords = generator.generate_multiple(
                    count=count,
                    length=16,
                    use_uppercase=True,
                    use_lowercase=True,
                    use_numbers=True,
                    use_symbols=True,
                    exclude_similar=True
                )
                
                print(f"\n🔑 Generated {count} passwords:")
                for i, pwd in enumerate(passwords, 1):
                    strength = generator.calculate_strength(pwd)
                    label = generator.get_strength_label(strength)
                    print(f"{i:2d}. {pwd} ({label})")
                    
            except ValueError:
                print("❌ Please enter a valid number!")
                
        elif choice == "5":
            # Check password strength
            test_password = input("Enter password to check: ").strip()
            if test_password:
                display_password_info(test_password, generator)
            else:
                print("❌ Please enter a password!")
                
        elif choice == "6":
            print("👋 Thank you for using the Password Generator!")
            break
            
        else:
            print("❌ Invalid choice! Please select 1-6.")
        
        # Ask to copy to clipboard if available
        if choice in ['1', '2', '3'] and 'password' in locals():
            try:
                copy_choice = input("\n📋 Copy to clipboard? (y/n): ").lower()
                if copy_choice in ['y', 'yes']:
                    pyperclip.copy(password)
                    print("✅ Password copied to clipboard!")
            except ImportError:
                print("ℹ️ Clipboard functionality not available")

def command_line_mode():
    """
    Command line interface for the password generator
    """
    parser = argparse.ArgumentParser(description='Generate secure random passwords')
    parser.add_argument('-l', '--length', type=int, default=16, help='Password length')
    parser.add_argument('-n', '--number', type=int, default=1, help='Number of passwords to generate')
    parser.add_argument('--no-upper', action='store_true', help='Exclude uppercase letters')
    parser.add_argument('--no-lower', action='store_true', help='Exclude lowercase letters')
    parser.add_argument('--no-numbers', action='store_true', help='Exclude numbers')
    parser.add_argument('--no-symbols', action='store_true', help='Exclude symbols')
    parser.add_argument('--include-similar', action='store_true', help='Include similar characters (i,l,1,L,o,0,O)')
    parser.add_argument('-s', '--strength', choices=['weak', 'medium', 'strong', 'very-strong'], 
                       help='Generate password with predefined strength level')
    
    args = parser.parse_args()
    
    generator = PasswordGenerator()
    
    try:
        if args.strength:
            passwords = [generator.generate_from_strength(args.strength) for _ in range(args.number)]
        else:
            passwords = generator.generate_multiple(
                count=args.number,
                length=args.length,
                use_uppercase=not args.no_upper,
                use_lowercase=not args.no_lower,
                use_numbers=not args.no_numbers,
                use_symbols=not args.no_symbols,
                exclude_similar=not args.include_similar
            )
        
        for password in passwords:
            print(password)
            
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Command line mode
        command_line_mode()
    else:
        # Interactive mode
        interactive_mode()
