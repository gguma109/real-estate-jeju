-- 기존 테이블에 휴지통 기능(소프트 삭제)을 위한 컬럼 추가
-- 이 스크립트는 기존 데이터베이스 구조를 업데이트할 때 사용합니다.

ALTER TABLE rentals ADD COLUMN is_deleted BOOLEAN DEFAULT 0;
ALTER TABLE rentals ADD COLUMN deleted_at DATETIME;

ALTER TABLE notes ADD COLUMN is_deleted BOOLEAN DEFAULT 0;
ALTER TABLE notes ADD COLUMN deleted_at DATETIME;

ALTER TABLE ads ADD COLUMN is_deleted BOOLEAN DEFAULT 0;
ALTER TABLE ads ADD COLUMN deleted_at DATETIME;
