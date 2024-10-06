from db_instance import get_db
import services
import services.journal_service

db = get_db()

# Hw8NYH8yYaInwwir4ZYz


journal = services.journal_service.get_journal('Hw8NYH8yYaInwwir4ZYz')
print(journal.volumes[0].issues[0].title)

