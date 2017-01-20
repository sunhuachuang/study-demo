class Article < ApplicationRecord
  has_many :comments, dependent: :destroy # default has destroy
  validates :title, presence: true, length: { minimum: 5 }
end
