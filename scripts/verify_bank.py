"""Independent SQL execution and structural, explanation, provenance review checks."""
import hashlib,json,sqlite3,subprocess,sys
from pathlib import Path
r=Path(__file__).resolve().parents[1];path=r/'src/data/questions.json'
before=path.read_bytes();bank=json.loads(before)
assert len(bank)==1000 and len({q['id'] for q in bank})==1000
fingerprints=set(); sql_count=0
for q in bank:
 fp=''.join((q['question']+'|'+ '|'.join(sorted(q['choices']))).split()).lower()
 assert fp not in fingerprints,q['id'];fingerprints.add(fp)
 assert len(q['choices'])==len(set(q['choices']))==4
 assert 1<=q['answer']<=4
 assert q['type']=='original' and q['year'] is None and q['session'] is None
 assert len(q['explanation'])>=30 and q['verificationStatus']=='reviewed'
 c=q.get('calculation')
 if c and c['kind'].startswith('sql'):
  db=sqlite3.connect(':memory:');db.execute('CREATE TABLE T(v INTEGER)');db.executemany('INSERT INTO T VALUES (?)',[(v,) for v in c['rows']]);actual=db.execute(c['sql']).fetchone()[0];db.close()
  assert actual==c['result'],(q['id'],actual,c['result'])
  assert q['choices'][q['answer']-1]==str(c['result'])
  sql_count+=1
subprocess.run([sys.executable,str(r/'scripts/generate_bank.py')],check=True)
assert before==path.read_bytes(),'Non-deterministic generation'
print(f'PASS: 1000 structure/provenance/duplicate checks; {sql_count} actual SQLite queries; deterministic regeneration. SHA256 {hashlib.sha256(before).hexdigest()}')
